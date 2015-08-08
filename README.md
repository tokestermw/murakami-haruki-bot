# Murakami Haruki char-RNN Bot

Generates sample text using @karpathy's [char-RNN model](https://gist.github.com/karpathy/d4dee566867f8291f086) and Murakami Haruki's [temporary Q and A blog](http://www.welluneednt.com) as the Japanese training corpus.

Scrape the website by `python scrape.py`.

Simply run `python min-char-rnn.py` to print out some samples. This runs an infinite loop and doesn't save any results.

My favorite line so far:

**僕の小説でも楽しいか誌はそれを文章のヨーションに与えるとめにンっていたい世界がとても書きますか。**

Which *roughly* translates to:

**Whether my novels are entertaining is based on putting Yotion(?) into the writing.**

Some sample results (limits at 200 characters):
```
----
iter 105100, loss: 69.034657
----
 かな。僕もはちろんだかなので、いいとを言いてしまいます。しょっと逃げたせにはどういうこといとか識していた言えなも覚えては、意味です。
村上春樹拝
それの仕事をしかということならか、僕だいくらいうことです。新の辺の一作品ターが匂いは眠ったより誤発。
村上春樹拝
僕はちにつかたこのなんとっていただわったいです。うジースペイステレビヘズニュー引にありません。｢サランス有死につかれたらのないのです。名古い 
----
iter 105200, loss: 68.778249
----
 にはあるのではあります。大つだとに好きなのたな試しれて、僕の状況は同じ世界にそういう観宙が入っていてしまう渡題があるんです。人たちは、誰か冷手話をしていただけに向き、意志は限りません。最近崎うんというので、感をしいです。そうしても、とっけの中途中にはよろ次生きのあ、そうめていとまに考えていました。自分の責任はもわかります。
ヒートは「金端な奏記は昔からそういうしむね。人間ら放さぼっていくしません。 
----
iter 105300, loss: 68.590968
----
 ものはよく戦薦しつひとつかれらど、どうすが必要です。でも時間（小説を書いていることでする。高刊デイセシットから音楽ると思います。だんだかっています。ありませんが、もだろうのでいかれると、エ春樹拝
彼女子とライノルカー訳ありますく、会社の深い話をすより】生きる作業を開職号員をしないですよね。あなたは今なんですが、たというすぐらがんてけませんですよね。それがっきつもあれば、面白いというのに信想を読んで 
```