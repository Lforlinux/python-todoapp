###docker build with tag
```
docker build -t lforlinux/python-todoapp:1.0 .
```
###run the continer
```
docker run -p 5000:5000 lforlinux/python-todoapp:1.0
```
###how to access the application
```
curl http://localhost:5000/
```
###how to post an entry to the app
```
 curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "task=Write an article" http://127.0.0.1:5000/
```