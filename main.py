def analyze_friendships():
    facebook_friends = {"alice","bob", "charlie", "diana", "eve", "frank"}
    instagram_friends = {"bob", "charlie", "grace", "henry", "alice", "ivan"}
    twitter_friends = {"alice", "diana" , "grace", "jack","bob", "karen"}
    linkedin_friends = {"charlie", "diana","frank", "grace", "luke" , "mary"}

    results = {}
    # Your tasks:
    # 1. Find friends who are on ALL four platforms
    all_platforms = facebook_friends | instagram_friends | twitter_friends | linkedin_friends
    results['all_platforms'] = all_platforms
    # 2. Find friends who are ONLY on Facebook (not on any other platform)
    facebook_only = facebook_friends - instagram_friends - twitter_friends - linkedin_friends

    results['facebook_only'] = facebook_only
    # 3. Find friends who are on Instagram OR Twitter but NOT on both
    instagram_xor_twitter = (instagram_friends | twitter_friends) - (instagram_friends & twitter_friends)
    results['instagram_xor_twitter'] = instagram_xor_twitter
    # 4. Find the total unique friends across all platforms
    total_unique = len(all_platforms)
    results['total_unique'] = total_unique
    # 5. Find friends who are on exactly 2 platforms


    results["exactly_two_platforms"] = list(find_exactly_two_platforms(facebook_friends,instagram_friends,twitter_friends,linkedin_friends))





    # Return a dictionary with all results
    return results


def find_exactly_two_platforms(*sets):
    list_of_sets = list(sets)
    intersection_sets = []
    friends_on_two_platform = set()
    for i in range(len(list_of_sets)):
        for j in range(i+1, len(list_of_sets)):
            intersection_set = list_of_sets[i] & list_of_sets[j]
            intersection_sets.append(intersection_set)
            friends_on_two_platform = friends_on_two_platform.union(intersection_set)
    
   
    frnds_two_platform = list(friends_on_two_platform)

    for frnd in frnds_two_platform:
        ct = 0
        for tw in intersection_sets:
            if frnd in tw:
                ct = ct + 1
        if ct != 1:
            friends_on_two_platform.discard(frnd)
    
    return friends_on_two_platform
                




# Test your function
result = analyze_friendships()
print("All platforms:", result.get('all_platforms'))
print("Facebook only:", result.get('facebook_only'))


print("Instagram XOR Twitter:", result.get('instagram_xor_twitter'))
print("Total unique friends:", result.get('total_unique'))

print("Exactly 2 platforms:", result.get('exactly_two_platforms'))