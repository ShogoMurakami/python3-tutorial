import hashlib
import bcrypt

#SHA-256
dat = 'bitcoin' 
hs = hashlib.sha256(dat.encode()).hexdigest()
print("SHA-256: " + hs)

#bcrypt

#saltの生成
salt = bcrypt.gensalt(rounds=10, prefix=b'2a')

password = b'user_pass'

#passwordのハッシュ化
result_hash = bcrypt.hashpw(password, salt)

print("bcrypt: " + str(result_hash))
