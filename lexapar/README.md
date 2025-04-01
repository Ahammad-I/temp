 Steps to Run the Application in Docker
1️⃣ Build the Docker Image
Run the following command to build the Docker image:


docker build -t lexapar:latest .
2️⃣ Run the Docker Container
Run the following command to start the container:

 
docker run --name lexapar-app -d -p 8000:8000 lexapar
🔹 Access the Application
Once the container is running, open your browser and visit:
📌 Django Default Port (Localhost Link):
👉 http://127.0.0.1:8000/