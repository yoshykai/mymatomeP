def fileR(path): #テキストファイル読み込み
    k=""
    with open(path, "r") as f:
        k+=f.read()
    return k.strip()

def fileW(path,text): #テキストファイル上書き
    with open(path, "w") as f:
        f.write(text)

def fileA(path,text): #テキストファイル追加書き込み
    with open(path, "a") as f:
        f.write("\n"+text)

if __name__=='__main__':
    k = (fileR("test.txt"))
    print(k)
