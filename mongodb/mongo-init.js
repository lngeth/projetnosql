db.createUser(
  {
    user: "admin",
    pwd: "mypassword",
    roles: [
      {
        role: "readWrite",
        db: "mydb"
      }
    ]
  }
);