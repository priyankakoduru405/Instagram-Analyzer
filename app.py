import pandas as pd
import re

# Read raw CSV files
following_raw = pd.read_csv("following.csv", header=None)
followers_raw = pd.read_csv("followers.csv", header=None)

# Convert all rows into one text block
following_text = " ".join(following_raw[0].astype(str))
followers_text = " ".join(followers_raw[0].astype(str))

# Extract usernames using regex
following = re.findall(r"[a-zA-Z0-9._]+", following_text)
followers = re.findall(r"[a-zA-Z0-9._]+", followers_text)

# Keep only likely usernames
following = [u.lower() for u in following if "." in u or "_" in u]
followers = [u.lower() for u in followers if "." in u or "_" in u]

# Convert to sets
following_set = set(following)
followers_set = set(followers)

# Compare
not_following_back = following_set - followers_set
you_not_following = followers_set - following_set

# Print results
print("\n=== People you follow but they don't follow back ===")
for user in sorted(not_following_back):
    print(user)

print("\n=== People who follow you but you don't follow back ===")
for user in sorted(you_not_following):
    print(user)

print("\n=== Summary ===")
print("Following:", len(following_set))
print("Followers:", len(followers_set))
print("Mutual:", len(following_set & followers_set))
