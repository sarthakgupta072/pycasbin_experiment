import casbin

e = casbin.Enforcer("model.conf", "policy.csv")

sub = "lice"
obj = "data1"
act = "read"

if e.enforce(sub, obj, act):
    print("Allow")
else:
    print("deny")
