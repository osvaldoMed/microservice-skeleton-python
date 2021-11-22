# Microservice-skeleton-python
A MedTrainer project to provide an standardized setup for PYTHON based projects. It is based in docker and docker-compose.

## Local usage


### docker-compose override
In order to keep our `docker-compose.yml` file clean & simple env vars and
local settings have been moved to `docker-compose.override.yml.dist`, before
running docker-composer please copy `docker-compose.override.yml.dist` as
`docker-compose.override.yml` and feel free to change it as needed.
```
cp docker-compose.override.yml.dist docker-compose.override.yml
```

### Test executions
The process to run test has been simplified by adding a `test_sample.py` script for pytest in the `tests` directory

```
docker-compose -f docker-compose.yml -f docker-compose.override.test.yml up
```



### Run development environment and debugger
You can run development environment environment setting the entry point for debugpy in docker-compose.override.dev.yml and run

```
docker-compose -f docker-compose.yml -f docker-compose.override.dev.yml up -d
```
To attatch to the debugger make sure `port=5678` is set up and `.vscode/launch.json` is configured as follows with right `localRoot` and `remoteRoot` within Docker container.
```
{
  "configurations": [
    {
      "name": "Python: Remote Attach",
      "type": "python",
      "request": "attach",
      "port": 5678,
      "host": "0.0.0.0",
      "pathMappings": [
        {
          "localRoot": "${workspaceFolder}",
          "remoteRoot": "/app"
        }
      ]
    }
  ]
}

```

### Run production

```
docker-compose -f docker-compose.yml -f docker-compose.override.prod.yml up -d
```

### Flask API skeleton example

Here is a link for an API example that implements the debugger and testing from this microservice-skeleton.

https://github.com/osvaldoMed/flask-api-skeleton
