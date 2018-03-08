FROM jjeffryes/kb_python3:latest
MAINTAINER KBase Developer


RUN kb-sdk version

# -----------------------------------------
# RUN conda config --add channels  https://conda.anaconda.org/rdkit && \
#    conda install -y nose \
#                     cairo \
#                     nomkl \
#                     rdkit

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

RUN grep response_body lib/BiochemistryAPI/BiochemistryAPIServer.py


CMD [ ]
