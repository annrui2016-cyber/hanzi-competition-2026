# 2026 汉字大赛 · 备赛营 · 2026 Chinese Character Challenge Prep

面向阿联酋中小学中文学习者的**汉字大赛备赛小工具**。学生按组别(Cycle）选择，按官方字词总表的 **基础 / 认读 / 书写** 三类分类练习。完全离线、单文件、手机电脑通用。

## 组别与内容（官方字词总表，580 条）

| Cycle | 基础 | 认读 | 书写(听写) | 小计 |
|---|---|---|---|---|
| **1 小学 Primary** | 30 | 70 | 30 | 130 |
| **2 初中 Middle** | 40 | 120 | 40 | 200 |
| **3 高中 High** | 40 | 160 | 50 | 250 |

字词表**单字 + 词**共 237 条唯一内容（131 单字 + 106 词）。

## 学习方式

- **基础 / 认读（不书写）**：每条 → 呈现（汉字/词 + 拼音 + 英文 + 发音）→ **听音选字**小练习（听发音、四选一）
- **书写（听写）**：呈现 → 逐字 **笔顺动画 → 描红 → 默写评分**（词逐字书写），复用「汉字轻松学」模式
- 进度按 组别×类别×字词 存于浏览器 localStorage

> 界面预留阿拉伯语字段（`ar`），后续可补充中英阿三语。

## 项目结构

```
index.html                  # 构建产物 = 部署的单文件应用（Vercel serve）
build.py                    # 构建脚本：python build.py
tool/index.template.html    # 源码模板
vendor/hanzi-writer.min.js  # HanziWriter v3.5.0 引擎（内嵌）
data/
  dasai_data.json           # 3 组别 × 3 类别 × 字词（拼音/英文/阿语/组成字）
  chardata.json             # 258 字的笔画路径与中线数据
```

## 构建

```bash
python build.py
```

## 数据来源

- 字词：2026 汉字大赛官方字词总表
- 笔顺：[Make Me a Hanzi](https://github.com/skishore/makemeahanzi) / [HanziWriter](https://hanziwriter.org)

---

Designed by **Dr. Zhou Fang** · dr.zhou.fang@gmail.com
