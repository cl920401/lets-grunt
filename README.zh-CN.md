# Let's Grunt

[English](README.md) · 简体中文

先规划，再动工作区；先复核骨架，再写业务逻辑。Let's Grunt 为 Codex 提供四个工程技能，帮你明确边界、落定契约，并做独立验收。

| 在 Codex 中调用 | 做什么 | 不做什么 |
| --- | --- | --- |
| `$lg-plan` | 只读讨论目标、范围和取舍 | 不写文件，不派发执行 |
| `$lg-spec` | 在授权的文档路径写规格、验收条件和交接卡 | 不写实现、测试、配置或可执行迁移 |
| `$lg-build` | 按锁定的规格实现授权切片，先复核可运行的空函数与伪代码 | 不跳过独立复核，不把执行权限当成推送或发布权限 |
| `$lg-refine` | 做一项范围明确、保持契约的小改动，执行针对性回归 | 不改契约，不擅自扩范围 |

每次单独进入一个模式，不自动跳转。支持 `agents/openai.yaml` 的 Codex 主机上，Spec、Build、Refine 只能显式调用，Plan 保持主机默认。这限制的是技能选择，不是文件访问；要强制规划阶段只读，请使用主机的只读沙箱。

## 安装与移除

先查看[四个技能](skills)和[共用工作流](skills/lg-spec/references/WORKFLOW.md)。在 macOS 或 Linux 上，于解包后的目录执行：

```sh
(
  set -eu
  dest="$HOME/.agents/skills"
  for n in lg-plan lg-spec lg-build lg-refine; do
    if [ -e "$dest/$n" ] || [ -L "$dest/$n" ]; then
      printf 'Already exists; not overwriting: %s\n' "$dest/$n" >&2
      exit 1
    fi
  done
  mkdir -p "$dest"
  for n in lg-plan lg-spec lg-build lg-refine; do
    cp -R "skills/$n" "$dest/"
  done
)
```

只在某个项目使用时，把目标换成该仓库下 `.agents/skills` 的绝对路径，不要两处都装。四个目录必须同级一起复制，包括 `agents/` 和 `lg-spec/references/WORKFLOW.md`；它们不是四个独立发包的技能。新开 Codex 会话，确认每个名字只出现一次，然后在临时项目试用 Plan。[Codex 技能文档](https://developers.openai.com/codex/skills)说明发现与调用策略，[Agent Skills 规范](https://agentskills.io/specification)说明文件格式。此项目以 Codex 为目标，其他客户端不在验证范围内。

卸载或升级时，只把这四个已安装的目录移出技能搜索路径，另行备份。不要删除整个技能目录。旧工具不会被此安装改动。

## 找不到命令怎么办

- 在目标项目新开 Codex 会话，确认每个技能目录都含同名 `SKILL.md`，不要把整个解包目录嵌套进技能根。
- 名称重复时检查用户级、项目级技能目录和已启用插件，只留预期的那份。
- 找不到共用工作流时，补回 `lg-spec/references/WORKFLOW.md`，保证四个目录同级。不要把规则复制进项目后绕过检查。

## 用一个小 CLI 试跑

分别在 Codex 输入下面四条，而不是在终端执行：

1. `$lg-plan 规划一个把标题转成短名的本地 CLI；不联网、不持久化、不写文件。`
2. `$lg-spec 只写 docs/SPEC.md，定义 CLI 输入输出、错误、验收及开发和复核交接。`
3. `$lg-build 按锁定版本的 docs/SPEC.md 只实现这条 CLI 链路。先交能运行的骨架和伪代码，独立复核通过再写业务。`
4. `$lg-refine 只优化现有测试的失败消息，不改变 CLI 的对外行为。`

[示例骨架和验收矩阵](examples/slug-skeleton/README.md)说明写业务代码前应核对什么。包结构和示例检查：

```sh
python3 scripts/check.py
```

非平凡的跨会话交接可用 [CHANGE.md 模板](skills/lg-spec/references/CHANGE.md)，在授权位置记录已锁定输入、复核证据和下一步。同一会话里的微小变更不用另建文档。跨上下文只传已锁定引用、硬约束和必要证据，独立复核默认不带原聊天或开发结论。

[验证记录](VALIDATION.md)说明实际跑过的检查；维护者可参考[发布核对单](RELEASE-CHECKLIST.md)。

## 许可

[MIT](LICENSE)。
