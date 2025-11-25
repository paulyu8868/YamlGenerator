import pandas as pd
import yaml
from pathlib import Path


def columnType(series): # 해당 컬럼의 type 반환
    # null 제거
    series = series.dropna()
    
    if len(series) == 0:
        return {'type': 'string'}  # 디폴트: string
    
    # 컬럼 Data Type
    dtype = series.dtype
    
    # 숫자타입
    if pd.api.types.is_integer_dtype(dtype) or pd.api.types.is_float_dtype(dtype):
        return {'type': 'number'}
    
    # Date, DateTime 체크
    sample = series.iloc[0] # 샘플 데이터 추출
    hyphenCnt = sample.count('-')
    timeDivCnt = sample.count(':')

    if hyphenCnt==2 and timeDivCnt>=2: # DateTime
        return {'type': 'string', 'format': 'date-time'}
    elif hyphenCnt==2: # Date
        return {'type': 'string', 'format': 'date'}
    
    # 모두 아니면 string
    return {'type': 'string'}

def generate_schema_from_csv(objectName):

    path = Path(f'csv/{objectName}.csv') # 파일 경로

    if not path.exists():
        print(f"존재하지 않는 파일: {path}")
        return None

    df = pd.read_csv(path) # csv 읽기
    
    properties = {} # 필드 정보들 담는 딕셔너리
    
    for column in df.columns:
        series = df[column] # 한 컬럼 데이터 추출
        field_type_info = columnType(series)
        properties[column] = field_type_info
    

    # Build schema structure
    schema = {
        'openapi': '3.0.3',
        'components': {
            'schemas': {
                objectName: {
                    'type': 'object',
                    'properties': properties
                }
            }
        }
    }
    return schema

def schemaToYaml(schema, path):
    # dictionary -> yaml 변환
    if path.exists():
        print(f"이미 존재하는 파일: {path}")
        return
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(schema, f, default_flow_style=False, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":

    '''
    ==========  사용법  ==========

    1. 변환할 csv 파일을 모두 csv 폴더에 오브젝트 명으로 저장. (yaml 파일의 오브젝트명에 활용됨)
    예시) PRODUCT.csv

    2. 해당 파일 실행 후 yaml 폴더 확인.
    
    ==============================
    '''

    # csv 폴더에서 변환할 파일 목록 불러오기
    path = Path('csv')
    objects = [file.stem for file in path.iterdir()] # 오브젝트명으로 저장

    for object in objects:
        # 스키마 생성
        schema = generate_schema_from_csv(object)
        yamlPath = Path(f'yaml/{object}.yaml')
        schemaToYaml(schema,yamlPath)






