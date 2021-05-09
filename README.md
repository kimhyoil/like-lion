## Django

💡 [Notion](https://www.notion.so/f8a4d2b76c174c8db3ca1657a2f736a4?v=06c5db69ce43403d86860619e825f238)

![image](https://user-images.githubusercontent.com/23691938/116989670-03828e80-ad0d-11eb-93ed-229a9eb8d334.png)

## Docker

- 리눅스 컨테이너 기반의 프로세스 격리화 툴
- CI/CD 를 효율적으로 도와주는 컨테이너 기반 가상화 플랫폼
- 장점
    - 용량 적음
    - 속도 향상
- Docker Image
    - 컨테이너를 실행 할 수 있는 실행파일 및 설정 값
- Container(컨테이너)
    - 격리된 공간에서 프로세스가 동작하는 환경
- Docker File
    - Docker Image를 만들기 위한 설정 파일
    - 빌드하면 자동으로 이미지 생성 → 배포 자동화
    - WORKDIR 에서 절대경로를 권장하는 이유?

    ```docker
    FROM python:3
    RUN pip3 install django  # 
    WORKDIR ./usr/src/app     # WROKDIR==cd (dir 이동 및 생성)
    COPY . .                 # 현재 경로의 파일들을 위 경로로 복사
    WORKDIR ./mytestsite      # 컨테이너의 작업 경로를 /usr/src/app/mytestsiste로 이동
    CMD ["python3", "manage.py", "runserver", "0:8000"]
    EXPOSE 8000
    ```

- Docker Compose
    - 여러 개의 컨테이너로 구성된 애플리케이션을 하나의 파일에 정의하여 관리 할 수 있는 기능

    ```yaml
    services:
      web:
        build: . # Docker file path
        command: python manage.py runserver 0:8000 # 항상 실행 할 명령어
        ports:
          - "8000:8000"
        volumes:
          - .:/web
        depends_on: # web 실행 전 실행 할 것
          - db
      db:
        image: postgres
        environment: # 환경 변수 설정
          - POSTGRES_USER=postgres
          - POSTGRES_PASSWORD=postgres
    ```

## VM vs Docker

- 가상화
    - 향상된 컴퓨터 성능을 효율적으로 사용하기 위해
    - 여러 서비스를 한 서버에 돌리면 안정성에 문제 → 서버 가상화
- VM
    - Host OS 위 Hypervisor 위 Guest OS를 올려 가상화
    - 격리 레벨이 높기 때문에 보안 유리
- Container based
    - Host OS 위 Docker 엔진 위에서 동작
    - Host 커널 공유 → IO처리가 쉬워 성능 상스
![image](https://user-images.githubusercontent.com/23691938/117579012-05dd5200-b12c-11eb-8d0b-943e5112b9cf.png)

## 명령어

- 이미지 조회
    - `docker image`
- 이미지 빌드
    - `docker build -t [repository]:[tag] [path]`
- 이미지 태깅
    - `docker tag [image id] [respository or tag]`
- 이미지 삭제
    - `docker rmi [image id or tag]`
- 실행중인 컨테이너 조회
    - `docker ps`
- docker compose 파일 실행
    - `docker-compose up`
- 컨테이너 종료
    - `docker stop [container id]`
