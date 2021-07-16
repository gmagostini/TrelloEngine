# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3
LABEL tag="trelloengine:test"
# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app/trelloengine
COPY . /app

EXPOSE 5001





# Creates a non-root user and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN useradd appuser && chown -R appuser /app
USER appuser



# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["python", "trelloengine/application.py"]
#CMD ["bash","waitress-serve --call 'application:create_app'"]
#CMD ["cd","trelloengine"]
#CMD ["ls","trelloengine"]
#CMD ["waitress-serve","application:create_app"]
CMD ["python", "application.py"]

