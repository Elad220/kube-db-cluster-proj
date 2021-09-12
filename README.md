# kube-db-cluster-proj
The project creates a new cluster which holds a MySQL DB, a job to populate it with the add_to_book.txt records, a service program which runs on a pod to wait and listen for a read request from the outside of the cluster, and a start_project script which initiates the request to start the reading process.
Note: this project was done using minikube and hyperkit as a vm provider, and scripts written in Python.
