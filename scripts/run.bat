.\.venv\Scripts\activate

python .\scripts\find_and_click.py --continuous ".\scripts\easy apply lightning.png" ".\scripts\easy apply.png" ".\scripts\mag.png" ".\scripts\go to search.png" ".\scripts\next.png" ".\scripts\submit.png" --confidence=0.9 --region 400 200 800 600 --close-window ".\scripts\go to search.png"
