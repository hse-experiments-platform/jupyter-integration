import os, nativeauthenticator

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

c.DockerSpawner.image = os.environ['DOCKER_JUPYTER_IMAGE']

network_name = os.environ["DOCKER_NETWORK_NAME"]
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = network_name

notebook_dir = os.environ["DOCKER_NOTEBOOK_DIR"]
c.DockerSpawner.notebook_dir = notebook_dir
c.DockerSpawner.volumes = {"jupyterhub-user-{username}": notebook_dir}

c.DockerSpawner.remove = True

c.JupyterHub.cookie_secret_file = "/data/jupyterhub_cookie_secret"
c.JupyterHub.db_url = "sqlite:////data/jupyterhub.sqlite"

c.JupyterHub.hub_ip = "jupyterhub"
c.JupyterHub.hub_port = 8080

c.Authenticator.admin_users = {'user'}
#c.LocalAuthenticator.create_system_users = True
c.JupyterHub.authenticator_class = 'native'
c.JupyterHub.template_paths = [f"{os.path.dirname(nativeauthenticator.__file__)}/templates/"]