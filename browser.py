import json
import requests
import sys

def get_all_repos(url):
	req = requests.get("http://" + url+"/v2/_catalog")

	parsed_json = json.loads(req.text)

	repo_array = parsed_json['repositories']

	return repo_array

def search_for_repo(url, repo_search_name) :

	repo_array = get_all_repos(url);

	repo_dict_search = {}

	if repo_search_name in repo_array:
		parsed_repo_tag_req_resp = get_tags_for_repo(url, repo_search_name)
		repo_dict_search[repo_search_name] = parsed_repo_tag_req_resp
	else:
		''' Get all the repos '''
		repo_dict = get_all_repo_dict(url, repo_array) 

		if any(False if key.find(repo_search_name)==-1 else True for key in repo_dict) ==  True:
			print "available options:- " 
			for key in repo_dict:
				if(key.find(repo_search_name)!=-1):
					repo_dict_search[key] = get_tags_for_repo(url, key)

					
	return repo_dict_search

def get_tags_for_repo(url, repo):
	repo_tags_url = "http://" + url + "/v2/" + repo  + "/tags/list"

	repo_tag_url_req = requests.get(repo_tags_url)
	parsed_repo_tag_req_resp = json.loads(repo_tag_url_req.text)
	return parsed_repo_tag_req_resp["tags"]
	
def get_all_repo_dict(url, repo_array):
	repo_dict = {}
	for repo in repo_array:
 		parsed_repo_tag_req_resp = get_tags_for_repo(url, repo)
 		repo_dict[repo] = parsed_repo_tag_req_resp

 	return repo_dict


def decorate_list(repo_dict):
	decorated_list_values = ""
 	
	if(len(repo_dict)==0):
		return "No results!"
		
	counter = 1;
 	for repo_key in repo_dict:
 		decorated_list_values +=  "\n-----------" + "\n" + str(counter) + ") Name: " + repo_key
 		decorated_list_values += "\nTags: "
 		counter+=1;
 		for tag in repo_dict[repo_key]:
 			decorated_list_values += tag + '\t'
 	
 	decorated_list_values += "\n\n" + str(counter-1) + " images found !"
 	return decorated_list_values

def usage():
 	return "Usage: browser.py <registry_endpoint> <keyword> <values> \n valid keywords : search, list, gettag"

if __name__ == "__main__":
	len_sys_argv = len(sys.argv[1:])

	if len_sys_argv < 3:
		print usage()
	elif len_sys_argv == 3:
		regurl = sys.argv[1:][0]
		keyword = sys.argv[1:][1]
		repo_to_search = sys.argv[1:][2]

		if keyword=="search":
			print decorate_list(search_for_repo(regurl, repo_to_search))
		elif keyword=="list":
			list_all = get_all_repo_dict(regurl, get_all_repos(regurl))
			print decorate_list(list_all)
		else:
			print usage()


