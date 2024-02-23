# משחק בסיסי ברח מהכפכף! 🪳🪳🪳

## סקירה כללית

הסקריפט הוא משחק פשוט של בסגנון התחמקות שנוצר באמצעות ספריית Pygame, שבו השחקן שולט בדמות (ה"שחקן") שצריך להימנע מהתנגשות עם אויבים המתקדמים לעברו. יש שני סוגים של אויבים ("EnemyLeft" ו-"EnemyRight") הנעים מטה במסך. השחקן יכול לזוז בכל הכיוונים כדי להתחמק מהאויבים. אם מתרחשת התנגשות, המשחק נגמר.

## דרישות

- Python 3.x
  ספריית Pygame

כדי לבדוק האם Python מותקן על המחשב המקומי שלך, הרץ:

```shell
python --version
```

כדי להתקין את Pygame, הרץ:

```shell
pip install pygame
```

## הרצת המשחק באופן מקומי

  ודא ש-Python ו-Pygame מותקנים במערכת שלך.
  שמור את הסקריפט בקובץ, לדוגמא, `game.py`.
  הנח את התמונות `Flip-flop.png` ו-`Cockroach.png` באותו תיקייה עם הסקריפט שלך.
  הרץ את הסקריפט עם Python על ידי הרצת:

```shell
python game.py
```

## כיצד פועל המשחק

### איתחול

כאשר הסקריפט מתחיל, הוא מאתחל את Pygame, מגדיר את המסך עם רקע תכלת ויוצר חלון משחק עם גובה ורוחב מוגדרים. אז הוא מאתחל את דמות השחקן ושתי דמויות של אויבים, כמו גם קבוצות ספרייט לניהול כל ישויות המשחק.

## מהלך המשחק

השחקן משתמש במקשי החצים כדי להזיז את הדמות במסך. האויבים (`EnemyLeft` ו-`EnemyRight`) זזים מראש המסך לכיוון התחתית בקצב קבוע, ומקום הופעתם משתנה בתוך טווח נתון.

אם דמות השחקן פוגשת באחת מן הדמויות האויבים, המסך הופך לאדום, המשחק מתעכב לשנייה ואז יוצא.

## לולאת עדכון

בכל פריים, המשחק טופל אירועי קלט מהמשתמש ומעדכן את מיקום השחקן והאויבים בהתאם למצב הנוכחי. כיוון תנועת האויבים מוגדר על ידי בחירה אקראית שנעשית כל שנייה.  
