
def solution(genres, plays):
    genre_dict = {} # [genre_dict] key = 장르 , value = [(횟수, index),...]
    cnt_dict = {} # [cnt_dict] key = 장르, value = 횟수의 합
    
    for i in range(len(genres)):
        cur_genre = genres[i] # 장르
        cur_play = plays[i] # 횟수
        
        # [genre_list] genre_dict에서 해당 key에 대한 'value를 가진 list'
        genre_list = genre_dict.get(cur_genre,[])
        genre_list.append((cur_play,i))
        genre_dict[cur_genre] = genre_list
        
        cnt_dict[cur_genre] = cnt_dict.get(cur_genre, 0) + cur_play
    
    # [cnt_sort_list] cnt_dict의 (key,value) 형식의 튜플을 원소로 가지는 리스트,
    # sorting을 위해 생성함.
    cnt_sort_list = list(cnt_dict.items())
    # 두번째 원소 기준으로 sort, 큰수부터 정렬하기 위해 reverse
    cnt_sort_list.sort(key=lambda tup: tup[1], reverse = True)
    ans = []
    
    for genre in cnt_sort_list:
        genre_list = genre_dict[genre[0]]
        # k[0]= 횟수 , k[1]= index (횟수는 큰수부터 인덱스는 작은 수부터 하기 위해 -k[1]처리 & reverse)
        genre_list.sort(key=lambda k: (k[0], -k[1]), reverse=True)
        
        # 두개씩만 뽑기 위해 [:2]처리
        for data in genre_list[:2]:
            ans.append(data[1])
        
    return ans
