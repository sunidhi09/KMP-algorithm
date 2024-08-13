def KMPSearch(pat,txt):
    m=len(pat)
    n=len(txt)
    lps=[0]*m
    j=0
    computelps(pat,m,lps)
    i=0
    results=[]
    while i<n:
        if pat[j]==txt[i]:
            i+=1
            j+=1
        if j==m:
            results.append(i-j)
            j=lps[j-1]
        elif i<n and pat[j]!=txt[i]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1
    if results:
        for result in results:
		    print("Found pattern at index",result)
    else:
        print("Pattern not found")
def computelps(pat,m,lps):
    l=0
    lps[0]=0
    i=1
    while i<m:
        if pat[i]==pat[l]:
            l+=1
            lps[i]=l
            i+=1
        else:
            if l!=0:
                l=lps[l-1]
            else:
                lps[i]=0
                i+=1
txt=input("Enter the pattern").strip()
pat=input("Enter the string").strip()
KMPSearch(pat,txt)