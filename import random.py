import random
import time

def wait():
    time.sleep(1)

def game_over(reason):
    print("\n💀 GAME OVER 💀")
    print("理由:", reason)
    print("👉 トイレ神に見放された…\n")
    exit()

print("🚽💀 トイレ神RPGへようこそ…")
wait()

name = input("勇者の名前を入力せよ：")
wait()

print(f"\n{name}よ…今、試練の時が来た…")
wait()

# 初期ステータス
paper = random.randint(0, 3)
luck = random.randint(1, 100)

print(f"\n🧻 トイレットペーパー残量: {paper}")
print(f"🍀 運: {luck}\n")
wait()

print("🚪 トイレに入った…")
wait()

# 第一選択
print("\nどうする？")
print("1: 座る")
print("2: 一旦スマホを見る")
choice = input(">> ")

if choice == "2":
    if random.random() < 0.5:
        game_over("スマホに夢中でタイミングを逃した")
    else:
        print("📱 神回避！ベストタイミングで戻った")
        wait()

# メインイベント
print("\n⚡ その時…波が来た！！")
wait()

if luck < 30:
    print("😱 嫌な予感がする…")
    wait()

# 紙チェック
if paper == 0:
    print("🚨 紙がない！！！")
    wait()
    print("どうする？")
    print("1: 諦める")
    print("2: 代替手段を探す")
    c = input(">> ")

    if c == "1":
        game_over("諦めた（精神的敗北）")
    else:
        if random.random() < 0.5:
            game_over("無謀な挑戦で状況が悪化")
        else:
            print("✨ 奇跡的に紙を発見！")
            paper = 1
            wait()

# 最終判定
print("\n🌀 運命の瞬間…")
wait()

score = luck + paper * 20 + random.randint(-20, 20)

if score > 120:
    print("👑 神エンド：完全勝利")
    print("👉 史上最高のコンディションで全てがうまくいった")
elif score > 80:
    print("✨ 大成功エンド")
    print("👉 安定した勝利。文句なし")
elif score > 50:
    print("🙂 普通エンド")
    print("👉 可もなく不可もなく")
elif score > 20:
    print("😱 危機回避エンド")
    print("👉 ギリギリ助かった…")
else:
    game_over("制御不能。すべてが終わった")

# ランダムおみくじ要素
print("\n🎲 トイレ神のお告げ…")
omens = [
    "今日は水を多めに飲め",
    "その椅子、冷たいぞ",
    "油断するな…第2波が来る",
    "外出先では慎重に",
    "その判断、正しかったのか？",
    "誰も見ていない…だが神は見ている"
]
print("📜", random.choice(omens))

print("\n🎉 プレイありがとう！もう一度やる？（再実行してね）")