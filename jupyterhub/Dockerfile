FROM quay.io/jupyterhub/jupyterhub

COPY jupyterhub_config.py .

RUN pip install \
    dockerspawner==0.10.0 \ 
    jupyterhub-nativeauthenticator

# ARG USER=user
# ARG PASS="user"
# RUN useradd -m -s /bin/bash $USER && echo "$USER:$PASS" | chpasswd