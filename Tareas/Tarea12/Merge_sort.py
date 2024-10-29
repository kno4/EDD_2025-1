def merge_sort(data):
    if len(data) > 1:
        mid = len(data) // 2
        izq = data[0:mid:1]
        der = data[mid::]
        print(f"{izq} ---  {der}")
        merge_sort(izq)
        merge_sort(der)
        i = d = k = 0
        while i < len(izq) and d < len(der):
            if izq[i] < der[d]:
                data[k] = izq[i]
                i += 1
            else:
                data[k] = der[d]
                d +=1
            k += 1
        while i < len(izq):
            data[k] = izq[i]
            i += 1
            k += 1
        while d < len(der):
            data[k] = der[d]
            d +=1
            k += 1
    print(f"Regreso de rec: {data}")
    return data
print(".-.-.-.-.-.-.MERGE-.-.-.-.-.-.-")
info = [8, 17, 89, 45, 34, 27, 899, 962, 35, 14, 2, 46]
print(merge_sort(info))

print("SUMA RECURISVA")