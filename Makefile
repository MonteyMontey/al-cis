dep:
	if [ ! -d "env" ];then virtualenv env;fi
	env/bin/pip install -r requirements.txt

proto:
	env/bin/python -m grpc_tools.protoc -Ial-proto --python_out=. --grpc_python_out=. al-proto/protocol.proto

run:
	PROMETHEUS_PORT=4444 GRPC_PORT=5000 MASTER_ADDRESS='localhost:3000' HOST='localhost' env/bin/python main.py

image:
	docker build -t al-cis .

checkformat:
	env/bin/pycodestyle $$(ls | grep '.*\.py' | grep -v '.*pb2.*')

autoformat:
	env/bin/autopep8 -ia $$(ls | grep '.*\.py' | grep -v '.*pb2.*')

docker-push:
	echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
	docker tag al-cis monteymontey/al-cis:latest
	docker push monteymontey/al-cis:latest

docker-push-dev:
	echo "${DOCKER_PASSWORD}" | docker login -u "${DOCKER_USERNAME}" --password-stdin
	docker tag al-cis monteymontey/al-cis-dev:latest
	docker push monteymontey/al-cis-dev:latest