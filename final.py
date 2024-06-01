import json


l = []
def sort_specific(files):
    for f2 in files:
        
        with open(f"{f2}",'r') as f:
            data = json.load(f)
        
            for i, v in data.items():
    
            
                    
                if "b1" in v.lower():
                    l.append(i.split(".jpg"))
                        
                if "b2" in v.lower():
                    l.append(i.split(".jpg"))
                
                if "a1" in v.lower():
                    
                    l.append(i.split(".jpg"))
                    
                if "a2" in v.lower():
                    l.append(i.split(".jpg"))
            
            
                    

    return l

result = sort_specific(["./extractedtext.json", "./extractedtext2.json"])


needed_videos = []

for i in result:
    try:
        
        needed_videos.append(f"https://www.youtube.com/watch?v={i[0].split("/")[2]}")
        
    except Exception as e:
        
        needed_videos.append(f"https://www.youtube.com/watch?v={i[0]}")


print(needed_videos)
        


