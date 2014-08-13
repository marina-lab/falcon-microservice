FROM marina/python:2.7.8_r1
MAINTAINER sprin

# Add and install Python modules
ADD requirements.txt /src/requirements.txt
WORKDIR /src
RUN pip install -r requirements.txt

# Bundle app source
ADD . /src
RUN chmod +x /src/start_uwsgi.sh

# Expose
EXPOSE  8080

# Run
CMD ["/src/start_uwsgi.sh"]
