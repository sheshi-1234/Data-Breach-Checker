import requests, json, argparse

parser=argparse.ArgumentParser(description="BreachCheck - check authorized accounts against BreachDirectory API")
parser.add_argument("-t","--target",required=True,help="Target email or username")
parser.add_argument("-oR","--output-raw")
parser.add_argument("-oN","--output-normal")
args=parser.parse_args()

def load_key():
    with open("conf.json","r") as f:
        return json.load(f).get("BreachedDirectory")

def req_breachdirectory(target):
    key=load_key()
    if not key or key=="API-KEY":
        print("Please add your RapidAPI key in conf.json")
        return None
    headers={"X-RapidAPI-Key":key,"X-RapidAPI-Host":"breachdirectory.p.rapidapi.com"}
    r=requests.get("https://breachdirectory.p.rapidapi.com/",
                   headers=headers,params={"func":"auto","term":target},timeout=15)
    return r.json()

def main():
    ans=req_breachdirectory(args.target)
    if not ans or not ans.get("success",False):
        print("API call failed")
        return
    print(f"Found in {ans.get('found',0)} breaches")
    if args.output_raw:
        json.dump(ans,open(args.output_raw,"w"),indent=4)
    out=open(args.output_normal,"w") if args.output_normal else None
    for e in ans.get("result",[]):
        if e.get("password"):
            print("Password:",e["password"])
            if out: out.write("Password: "+e["password"]+"\n")
        if e.get("sha1"):
            print("SHA1:",e["sha1"])
            if out: out.write("SHA1: "+e["sha1"]+"\n")
    if out: out.close()

if __name__=="__main__":
    main()
