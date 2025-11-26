용도: Salesforce Data Cloud Ingestion API 생성 시 필요한 스키마(YAML 파일) 생성

예상 사용 시나리오: 태블로 프렙 > 데이터 클라우드 (Ingestion API 사용)

사용법

1. 해당 프로젝트 다운로드 후 csv, yaml 폴더 생성

2. csv 파일 출력
<img width="139" height="200" alt="image" src="https://github.com/user-attachments/assets/75b7ad95-fcca-40e4-ae7f-cd8499a064e4" />

- 프렙의 출력 화면에서 csv 파일을 먼저 추출


3. 추출한 csv 파일을 사용할 오브젝트명에 맞게 파일명 변경한 뒤 csv 폴더에 모두 저장

4. python 파일 실행시 yaml 폴더에 변환된 형태로 제공



TODO
- 1)int타입인 경우와 ID가 모두 숫자인 경우 인식 
- +)Description 기능 제공
- +)README 가이드 수정

Updates:
<2025.11.26>
- date 타입 인식 오류 수정
- ID 인식 오류 수정(float 타입만 number로 인식하도록 변경)

