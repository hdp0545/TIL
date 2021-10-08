# 2021-10-08 NoSQL

### NoSQL 이란?

- Not Only SQL

- CAP 이론

  - **consistency**
    - 일관성
  - **Abailability**
    - 가용성
  - **Partition tolerance**
    - 분산 가능

- 모두를 만족하는 DB는 없다..

  - CA

    - RDBMS

  - CP

    - Mongo DB

  - AP

    - Couch DB

      

### RDBMS와 ACID 속성

- **Atomicity**
  - 작업이 전부 반영되거나 안되어야 함
- **Consistency**
  - 늘 일관된 상태를 유지해야함
- **Isolation**
  - 여러 작업이 실행되더라도 그것이 순차적으로 실행되어야 함.
- **Durability**
  - 작업이 완료되었다면 영구적으로 반영되어야 함.



### NoSQL의 등장 배경

- 데이터센터가 여러곳에 분산되는 것이 일반적
- 덕분에 **Partition tolerance**가 중요한 가치로 인식됨
- consistency가 중요하지 않은 서비스들이 등장하면서 조금 더 availability가 보장하는 방법들이 소개되기 시작
  - ex) 페이스북의 경우 1~2초 다른 데이터가 나온다고 문제가 생기지 않음
- eventual consistency의 개념이 등장



### NoSQL의 특징

- 데이터간의 관계를 정의하지 않음
- 대용량의 데이터 저장 가능
- 분산형 구조
  - 덕분에 데이터 유실이나 서비스 중지가 없음
- 고정되지 않은 테이블 스키마



### NoSQL의 종류

- ##### Document Store

  - json 기반의 데이터를 저장
  - 가장 널리 사용되는 데이터베이스
  - 쿼리와 비슷하게 데이터 검색 가능
  - Mongo DB가 대표적

- ##### Wide Column Store

  - 테이블의 각 칼럼이 key-value로 정의
  - SQL과 유사한 형태로 사용
  - 제약적인 Index 지원
  - 카산드라가 대표적

- key-value Store

  - key값을 통한 단순 조회만을 지원.
  - 주로 In memory의 경우, Session Store, Cache등의 목적에 많이 사용
  - Redis가 대표적

- Graph

  - 데이터간 관계표현에 강점

- Search Engine

  - 비정형 데이터 검색
  - 엘라스틱 서치가 대표적

- Time Series

  - 모니터링에 주로 사용되는 저장



### MongoDB OverView

- 가장 널리 사용되는 NoSQL
- Json기반의 Document Store
- Collection = Table
- Schemaless
- 고가용성 - ReplicaSet
  - 보통 3개의 서버로 2개가 레플리카로 운영되다가 마스터가 죽으면 2개의 레플리카중 하나가 마스터의 역할을 대신함
- 수평 확장성 - 샤딩
- Mongo CLI 제공



### Redis Overview

- Key 값을 사용한 단순 조회
- 다양한 Value data type 지원
  - String, List, Set, Hash
- Memory 기반으로 고성능 읽기/쓰기 성능 지원
- 고가용성 - Replication
  - 마스터 서버와 슬레이브를 사용하여 3개의 서버 운영
- 수평 확장성 - 클러스터링

- redis 메모리 관리 정책
  - 총 데이터양 이상의 메모리를 항상 사용할 수 있도록 설정해 줘야함.
  - Eviction Policy를 구성하여 필요없는 데이터를 자동삭제 해줘야 함.
- 데이터를 디스크에 저장하여 데이터 보존가능



### Database Selection

- 극복해야 할 중요 포인트를 중심으로 고려
  - 데이터 모델의 변경이 잦음
    - MongoDB
  - 데이터 발생이 폭발적 증가 예상
    - Elasticsearch, Cassandra
  - 고성능 캐시를 사용해야 함
    - Redis
  - 트랜잭션 보장이 가장 중요함
    - RDBMS
- 기타 제약 사항 검토
  - 비용, 기술 지원 수준등
  - 조회 패턴(조건의 복잡성.)

