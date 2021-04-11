## 스타트업 개발자 채용 大 박람회

(현재 준비중입니다.)

Seed ~ Series B에 있는 스타트업을 위한 채용정보 페이지입니다.  
Back-end, Frontend, Mobile 등 개발자를 대상으로 진행하고 있습니다.  
해당 스타트업에 종사하시는 분뿐만 아니라 채용 관련 정보를 알고 계시다면 PR을 해주세요!

## PR/스타트업 규칙

- Seed ~ Series B 이하인 Real 스타트업만 등록이 가능합니다. (Series C 이상 도달 시 채용 공고는 자동으로 삭제 처리될 수 있습니다.)
- [더브이씨](https://thevc.kr/SendBird)에 등록된 스타트업만 가능합니다.
- 회사 공식 or 서비스 웹페이지가 존재해야 합니다.
- 회사나 서비스 존재가 불확실하거나 명확하지 않은 경우, [잡플래닛](https://www.jobplanet.co.kr)에서 회사 점수가 낮다고 판단하는 경우, 가상화폐 거래, 대출, 보험, 금융 투자가 주 서비스로 확인되는 경우, 사람이 판단했을 때 이 회사는 좀 아니다 싶으면 PR이 거절될 수 있습니다.

## 스타트업 개발자 채용



## db.json

PR json 모델

```json
{
  "company": {
    "name": "좋은 회사",
    "link": "https://...com",
    "series-step": "SEED | A | B"
  },
  "recruit": {
    "link": "https://...com",
    "description": "좋은 회사에서 개발자를 모집합니다.",
    "developers": [
      {
        "category": "BACKEND | FRONTEND | ANDROID | IOS",
        "limit": "2021-05-21",
        "minimumCareer": [
          "ALL", // 상관없음
          "NEW", // 신입
          "YEAR_1", // 1년차 이상
          "YEAR_5" // 5년차 이상
        ],
        "minimumQualifications": [ // 최대 10개
            "개발을 잘 하시는 분", // 각 최대 100자
            "일을 잘 하시는 분"
        ],
        "preferredQualifications": [ // 최대 10개
            "롤 티어 골드 이상", // 각 최대 100자
            "해피해킹 사용하시는 분",
        ]
      },
      { ... },
      { ... }
    ]
  }
}
```
