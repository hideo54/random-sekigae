# random-sekigae

## 概要

前に行きたい人を前に行かせるという条件付きで、ランダムに席替えの座席を決定します。

## バージョン

Ver 1.0

## 使い方

1. data.json に、前に行きたい人の配列を "concerned" 、その他の人の配列を "normal" とし、書く。
```例:
{
    "normal": ["寿司"],
    "concerned": ["博多市"]
}
```
2. Python 2.6 以上の環境で sekigae.py を実行。

## 使用条件

* クラスの人数の合計が55人となる必要がある。55人は以下のように配置され、出力される:
```
|00|01|02|03|04|05|
|06|07|08|09|10|11|12|
|13|14|15|16|17|18|19|
:  :  :  :  :  :  :  :
|48|49|50|51|52|53|54|
```
* 全ての個人の苗字は全角3文字以下でなければならない。
* 出力は等幅フォント環境、および、日本語の全角文字がちょうど半角2つ分の幅で出力される環境を前提にしている。

## 連絡先

* Twitter: @hideo54
* E-mail: contact@hideo54.com
