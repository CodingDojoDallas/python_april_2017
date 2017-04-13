import md5
password = 'password'
encrypted_password = md5.new(password).hexdigest();
print encrypted_password;
