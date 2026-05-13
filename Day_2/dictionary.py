import json

data = {
    "nama depan": "",
    "nama belakang": "",
    "alamat": "",
    "umur": "",
    "hobby": ["", "", ""],
}

print(data["alamat"])
data["alamat"] = "Jogja"
print("\nSetelah diupdatae")
print(data)


BigData = [
    {
        "nama depan": "",
        "nama belakang": "",
        "alamat": "",
        "umur": "",
        "hobby": ["", "", ""],
    },
    {
        "nama depan": "",
        "nama belakang": "",
        "alamat": "",
        "umur": "",
        "hobby": ["", "", ""],
    },
    {
        "nama depan": "",
        "nama belakang": "",
        "alamat": "",
        "umur": "",
        "hobby": ["", "", ""],
    },
]
BigData.append(
    {
        "nama depan": "",
        "nama belakang": "",
        "alamat": "",
        "umur": "",
        "hobby": ["", "", ""],
    }
)

print(json.dums(BigData, index=4))
