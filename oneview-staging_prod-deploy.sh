echo Deploying to: $deploy_environment
echo `whoami`
NOW=`date +"%m-%d-%y_%H%M%S"`
echo $NOW
if [ $deploy_environment == "stg" ]
then
    aws ecr get-login --no-include-email --region us-east-1 --profile nonprod | bash
    FROM_IMAGE="052090234383.dkr.ecr.us-east-1.amazonaws.com/oneview:uat"
else
	FROM_ENV="stg"
    FROM_IMAGE="033910152575.dkr.ecr.us-east-1.amazonaws.com/oneview:stg"
    aws ecr get-login --no-include-email --region us-east-1 | bash
fi

docker pull $FROM_IMAGE

aws ecr get-login --no-include-email --region us-east-1 | bash
docker tag $FROM_IMAGE 033910152575.dkr.ecr.us-east-1.amazonaws.com/oneview:$deploy_environment
docker tag $FROM_IMAGE 033910152575.dkr.ecr.us-east-1.amazonaws.com/oneview:${deploy_environment}-${NOW}

docker push 033910152575.dkr.ecr.us-east-1.amazonaws.com/oneview

docker rmi 033910152575.dkr.ecr.us-east-1.amazonaws.com/oneview:${deploy_environment}-${NOW}
docker rmi 033910152575.dkr.ecr.us-east-1.amazonaws.com/oneview:$deploy_environment
docker rmi $FROM_IMAGE 

aws ecs update-service --cluster oneview-${deploy_environment} --service oneview-${deploy_environment} --desired-count 2 --force-new-deployment
echo $?

echo Done
