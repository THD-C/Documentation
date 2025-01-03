# [Mongo]

MongoDB container, which communicates with [Mongo Manager](https://github.com/THD-C/Mongo_Manager).
On startup inserts necessary data needed for system to function properly.

It automatically fetches application secrets like `COIN_GECKO_KEY` from private repository [Secrets](https://github.com/THD-C/Secrets/blob/main/THDC_secrets.json) and list of most common passwords stored in repository [Common_Passwords](https://github.com/THD-C/Common_Passwords).

During the **build** process `github_token` needs to be passed in order to authenticate to [Secrets](https://github.com/THD-C/Secrets/blob/main/THDC_secrets.json) repository.

`github_token` for development purposes can be created using shell command: `echo "$(gh auth token)" > .github_token`

## Data import mechanism
After mongoDB container startup all data specified in `/data` directory in `.json` files will be imported to mongoDB.

Each `.json` file defines singular collection. Collection name will be the same as the `.json` file name.

### Add custom data to DB
You need to add or modify existing file inside the `/data` directory and rebuild the docker image, that's it.

![image](/Picture/Example.png)
