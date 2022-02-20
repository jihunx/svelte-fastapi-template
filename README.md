# 설명
* Svelte(frontend), FastAPI(backend)로 만든 기본 웹사이트 템플릿입니다.
* Frontend에서 숫자를 입력하면 Backend에서 제곱한 값을 리턴하여 Frontend에서 결과를 표시합니다.

# 설치 및 실행
<pre>
docker-compose up -d
</pre>

브라우저에서 아래 주소로 접속
<pre>
http://localhost:4000
</pre>

# 구조
<pre>
svelte-fastapi-template
├─ frontend
│   ├─ node_modules
│   ├─ public
│   │   ├─ build
│   │   ├─ favicon.png
│   │   ├─ global.css
│   │   └─ index.html
│   ├─ scripts
│   ├─ src
│   │   ├─ App.svelte
│   │   └─ main.js
│   ├─ .gitignore
│   ├─ Dockerfile
│   ├─ package.json
│   ├─ package-lock.json
│   ├─ README.md
│   └─ rollup.config.js
├─ backend
│   ├─ Dockerfile
│   ├─ main.py
│   └─ requirements.txt
├─ .gitignore
├─ docker-compose.yml
├─ package-lock.json
└─ README.md
</pre>

# Svelte 실행 Port 변경
frontend > package.json 파일의 `port` 뒤의 숫자 수정
<pre>
"start": "sirv public --no-clear --host 0.0.0.0 --port 4000"
</pre>
