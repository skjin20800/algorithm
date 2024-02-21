from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_dict = defaultdict(list)

    # 장르별로 인덱스와 재생 횟수를 저장
    for index, (genre, play) in enumerate(zip(genres, plays)):
        genre_dict[genre].append((index, play))

    # 장르별로 재생 횟수 내림차순으로 정렬
    for genre in genre_dict:
        genre_dict[genre].sort(key=lambda x: x[1], reverse=True)

    # 장르별로 전체 재생 횟수 내림차순으로 정렬
    sorted_genres = sorted(genre_dict.keys(), key=lambda x: sum(play for _, play in genre_dict[x]), reverse=True)

    # 각 장르별로 최대 2개의 노래를 선택
    for genre in sorted_genres:
        answer.extend(song_index for song_index, _ in genre_dict[genre][:2])

    return answer
