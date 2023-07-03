IMAGE_PREFIX = 018288985300.dkr.ecr.ap-southeast-1.amazonaws.com
IMAGE_NAME = microstack-dramatiq
IMAGE_TAG = $(shell cat VERSION)

docker-build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) -f Dockerfile .
docker-run:
	docker run --rm -it  -e REDIS_PASSWORD=test --network=host $(IMAGE_NAME):$(IMAGE_TAG)
docker-shell:
	docker run --rm -it  -e REDIS_PASSWORD=test  --network=host --entrypoint=/usr/bin/bash $(IMAGE_NAME):$(IMAGE_TAG)
