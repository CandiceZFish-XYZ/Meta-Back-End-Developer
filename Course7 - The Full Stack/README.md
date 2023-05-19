# The Full Stack

## Production environment

### Deployment

- Mannual: FTP, SFTP
- Automatic deployment: configured with verson control system and build tools
- CI / CD: push code to repository, build tool creates a build environment that's identical to the production environment and runs tests, uploaded to server.

### Hosting

- Each Layer is hosted on one more multiple servers! (???)
- Pysical server vs virtual server (cloud computing)
  - Server & Serverless in cloud computing

### Virtual servers & containers

- hypervisor: software used for virtualization
  - Type 1 bare-metal hypervisor, a software layer, works directly with server hardware, efficient but complex to setup; KVM
  - Type 2, works on top of an operating system, slower but easy with management console and no dealing with hardware, Oracle VirtualBox
  -
- Containerization: pack dependencies and application, run regardless of the OS or hardware
  - Docker, one process or application per container
  - Pod, node, cluster
  - there's the management, deployment, networking, and scaling of these containers known as container orchestration - Kubernetes or K8s

### Self-hosted Cloud

- IaaS: on-demand infrastructura units
  - load balancer, servers, computing units, storage, virtualization
  - Popular IaaS include: AWS EC2, Google computing units, Digital Ocean and Azure virtual machines.
- PaaS: no need to manage servers; specialized cloud solution that offers essentials to develop, buid, host and run, including APIs, database, caching, file storage.
  - Ex: Meta (provides an API to use its proprietary services), AWS Elastic Beanstalk, Heroku, Cloudflare, Google app engine, Azure
- Saas: on-demand or pricing model subscription
- DBaaS: No need to mannually set up database, managing, optimizing and scaling.

### Cloud Computing

Cloud infra

- public cloud: pay as you go
  - on-demand pricing
  - quick availability
  - quick scalability / auto scalling
- private cloud: more security with tailored solution. Self-managed
  - Security, Control, Scalability, Reliability.
- Hybrid Cloud
  - less expensive than private cloud; complex set up.

Cloud computing elements

- Computing units: virtual machines
  - allocate cores or memories, some offer GPUs
  - volatile storage
- Storage
  - Purchase, perserve, discard
  - Object storage: get an API to upload and download; link expires
- Database: SQL, NoSQL, time series

### Scaling

- vertical
- horizontal

### Load balancing

- round-robin
  - distributes requests equally
- health-based

  - distributes only to available servers

- use reverse-proxy
  - serve static files as is (offload to CDN, improves page loading time)
  - then forward request to server

database scaling

- vertical scaling
- horizontal scaling
  - sharding:
    - db in multiple chunks, one db server holds one chunk, another keeps track of chunks
  - master-slave replication
    - requests are evenly distributed to slave servers
