url = input("Enter a full URL: ")

clean_url = url.replace("http://", "")

print("Cleaned URL:", clean_url)

parts = clean_url.split(".")

domain = parts[1]
print("Domain:", domain)

TLD = parts[2]

#We might get a trailling / character, so we need to remove it.
#TLD_clean = TLD.strip("/")
TLD_clean = TLD.replace("/", "")
print("Top-Level Domain:", TLD_clean)