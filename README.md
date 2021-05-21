## 스타트업 개발자 채용 大 박람회

Seed ~ Series B에 있는 스타트업을 위한 채용정보 페이지입니다.  
Back-end, Frontend, Mobile 등 개발자를 대상으로 진행하고 있습니다.  
해당 스타트업에 종사하시는 분뿐만 아니라 채용 관련 정보를 알고 계시다면 PR을 해주세요!

## 스타트업 개발자 채용

<table>
    <tr>
        <th width="150">회사명</th>
        <th width="120">투자단계</th>
        <th width="120">구분</th>
        <th width="120">마감일</th>
        <th width="120">최소경력</th>
        <th>링크</th>
    </tr>
    <tr>
        <td rowspan="1">
            <a href="https://ban-life.com" target="_blank">반려생활</a>
        </td>
        <td rowspan="1">SEED</td>
        <td>프론트엔드</td>
        <td>
            2021-06-15
            </td>
        <td>무관</td>
        <td><a href="https://ban-life.com/recruit" target="_blank">링크</a></td>
    </tr>
    <tr>
        <td rowspan="1">
            <a href="https://modusign.co.kr" target="_blank">모두사인</a>
        </td>
        <td rowspan="1">B</td>
        <td>백엔드</td>
        <td>
            2021-06-15
            </td>
        <td>무관</td>
        <td><a href="https://www.notion.so/975a991feaa44450bfb29c3832091c24" target="_blank">링크</a></td>
    </tr>
    <tr>
        <td rowspan="1">
            <a href="https://lvup.gg" target="_blank">빅픽처인터렉티브</a>
        </td>
        <td rowspan="1">B</td>
        <td>백엔드</td>
        <td>
            2021-05-31
            </td>
        <td>무관</td>
        <td><a href="https://www.wanted.co.kr/wd/43089" target="_blank">링크</a></td>
    </tr>
    
</table>

## 규칙

### 등록 가능한 스타트업 (모두 만족)

- Seed ~ Series B 이하의 스타트업
- [더브이씨](https://thevc.kr)에 등록된 스타트업
- 회사 또는 서비스 웹페이지가 존재하는 스타트업

### 등록 불가능한 스타트업

- 회사나 서비스 존재가 불확실하거나 명확하지 않은 경우
- [잡플래닛](https://www.jobplanet.co.kr)에서 회사 점수가 낮다고 판단하는 경우
- 가상화폐 거래, 대출, 보험, 금융 투자가 주 서비스로 확인되는 경우
- 사람이 판단했을 때 이 회사는 좀 아니다 싶은 경우

## PR

jobs 폴더에 아래와 같이 ${company_name}.json 파일을 생성하시면 됩니다.

모든 정보를 Github에 표시하지는 않으므로 텍스트를 너무 길게 작성하실 필요는 없습니다. (별도 웹 페이지 준비중)

```json
{
  "company": {
    "name": "반려생활",
    "link": "https://...",
    "series_step": "ENUM(SEED|PRE_A|A|B)"
  },
  "recruits": [
    {
      "description": "OO 개발자를 모집합니다.",
      "category": "ENUM(FRONTEND|BACKEND|ANDROID|IOS)",
      "limit_date": "yyyy-MM-dd",
      "link": "https://...",
      "minimum_career": "ENUM(ALL|NEW|YEAR_1~10)",
      "minimum_qualifications": [
        "요구사항"
      ],
      "preferred_qualifications": [
        "우대사항"
      ]
    },
    {},
    {}
  ]
}
```
