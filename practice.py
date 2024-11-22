import pandas as pd
import os

def create_html_table(source_file, output_file):
    """
    장비 데이터를 HTML 테이블 형식으로 변환하여 저장
    """
    try:
        # 원본 데이터 읽기
        df = pd.read_excel(source_file)
        
        # HTML 시작
        html_content = """
        <!DOCTYPE html>
        <html>
        <head>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            td {
                border: 1px solid black;
                padding: 4px;
                text-align: left;
                vertical-align: top;
            }
            .header {
                background-color: #f2f2f2;
            }
            .centered {
                text-align: center;
            }
        </style>
        </head>
        <body>
        <table>
        """
        
        # 4개씩 그룹화하여 처리
        for i in range(0, len(df), 4):
            group = df.iloc[i:i+4]
            
            # 사용부서 행
            html_content += "<tr>"
            for _ in range(4):
                html_content += "<td>사용부서</td>"
            html_content += "</tr>"
            
            # 관리번호 행
            html_content += "<tr>"
            for j in range(4):
                if j < len(group):
                    html_content += f"<td>관리번호</td>"
                else:
                    html_content += "<td></td>"
            html_content += "</tr>"
            
            # 계측기명 행
            html_content += "<tr>"
            for j in range(4):
                if j < len(group):
                    html_content += f"<td>계측기명</td>"
                else:
                    html_content += "<td></td>"
            html_content += "</tr>"
            
            # 품명 행
            html_content += "<tr>"
            for j in range(4):
                if j < len(group):
                    html_content += f"<td>품명</td>"
                else:
                    html_content += "<td></td>"
            html_content += "</tr>"
            
            # S/N 행
            html_content += "<tr>"
            for j in range(4):
                if j < len(group):
                    html_content += f"<td>S/N</td>"
                else:
                    html_content += "<td></td>"
            html_content += "</tr>"
            
            # Directed Korea 행
            html_content += "<tr>"
            for j in range(4):
                if j < len(group):
                    html_content += "<td class='centered'>Directed Korea</td>"
                else:
                    html_content += "<td></td>"
            html_content += "</tr>"
            
            # 빈 행 추가
            html_content += "<tr><td colspan='4'>&nbsp;</td></tr>"
        
        # HTML 종료
        html_content += """
        </table>
        </body>
        </html>
        """
        
        # HTML 파일로 저장
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        return f"HTML 테이블이 생성되었습니다: {output_file}"
        
    except Exception as e:
        return f"오류가 발생했습니다: {str(e)}"

def convert_html_to_excel(html_file, excel_file):
    """
    생성된 HTML을 Excel 파일로 변환
    """
    try:
        # HTML을 데이터프레임으로 읽기
        tables = pd.read_html(html_file)
        df = tables[0]
        
        # Excel 파일로 저장
        df.to_excel(excel_file, index=False)
        
        return f"Excel 파일이 생성되었습니다: {excel_file}"
        
    except Exception as e:
        return f"Excel 변환 중 오류 발생: {str(e)}"

# 실행 코드
source_file = '연구소_장비_관리_대장.xlsx'
html_output = 'equipment_table.html'
excel_output = '장비_라벨.xlsx'

# HTML 생성
print(create_html_table(source_file, html_output))

# Excel 변환
print(convert_html_to_excel(html_output, excel_output))