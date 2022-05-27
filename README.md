# ush-web
 Class Attendance Tracker

_disclaimer: this is an older project that I haven't made open source until now, don't mind the bad code_
 
## Requirements
- at least Python 3.6.1
- aiohttp & aiosqlite
- a reverse proxy server (nginx or openresty)

## Installation
nginx.conf
```
server {
    ...

    root /var/www/ush.3d1.ro;
    index index.php;
	
    location / {
        try_files $uri $uri/ @apachesite;
    }
	
    location @apachesite {
        proxy_set_header Host $host;
        proxy_pass http://127.0.0.1:2020;
    }
}
```

courses.db (sqlite3)
```sql
CREATE TABLE "courses" (
    `course` TEXT,
    `date_time` TEXT,
    `name` TEXT,
    UNIQUE(course, name)
)
```
