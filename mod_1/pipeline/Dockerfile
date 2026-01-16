# base docker image that we will build on
FROM python:3.13.11-slim

# set up our image by installing prerequisites
RUN pip install pandas pyarrow

# set up the working directory inside the container
WORKDIR /app
# copy the script to the workdir
COPY pipeline.py pipeline.py

# define what to do first when the container runs
ENTRYPOINT ["python", "pipeline.py"]