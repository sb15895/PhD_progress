The following list of items should be tried to be integrated into a talk covering your data centre, if possible. We hope your site's administrator will support you to gather the information with little effort.
https://hps.vi4io.org/events/2022/iodc

Workload characterisation: 
```
Scientific Workflow (give a short introduction)
    A typical use-case (if multiple are known, feel free to present more)
        Involved number of files/amount of data
    Job mix
        Node utilisation (related to peak-performance)

System view
    Architecture
        Schema of the client/server infrastructure
           Capacities (Tape, Disk, etc.)
        Potential peak-performance of the storage
            Theoretical
            Optional: Performance results of acceptance tests.
        Software/Middleware used, e.g. NetCDF 4.X, HDF5, …

    Monitoring infrastructure
        Tools and systems used to gather and analyse utilisation
    Actual observed performance in production
        Throughput graphs of the storage (e.g., from Ganglia)
        Metadata throughput (Ops/s)
    Files on the storage
        Number of files (if possible, per file type)
        Distribution of file sizes

Issues/Obstacles
    Hardware
    Software
    Pain points (what is seen as the most significant problem(s) and suggested solutions, if known)

Conducted R&D (that aim to mitigate issues)
    Future perspective
    Known or projected future workload characterisation
    Scheduled hardware upgrades and new capabilities we should focus on exploiting as a community
    Ideal system characteristics and how it addresses current problems or challenges
    What hardware should be added
    What software should be developed to make things work better (capabilities perspective)
    Items requiring discussion
``` 