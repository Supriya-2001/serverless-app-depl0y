FROM google/cloud-sdk:latest

RUN apt-get update && \
    apt-get install -y python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install google-cloud-functions

ENV PROJECT_ID=meta-sensor-380711
ENV FUNCTION_NAME=send_event_to_cloud_run
ENV REGION=us-central1
ENV RUNTIME=python39

WORKDIR /app

COPY main.py /app

CMD gcloud functions deploy $FUNCTION_NAME \
        --project $PROJECT_ID \
        --region $REGION \
        --runtime $RUNTIME \
        --entry-point main \
        --trigger-event google.storage.object.finalize
