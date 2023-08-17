-- list all privileges of MySQL users `user_0d_1` and `user_0d_2`
echo "CREATE USER 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p
echo "GRANT ALL PRIVILEGES ON . TO 'user_0d_2'@'localhost';" | mysql -hlocalhost -uroot -p
