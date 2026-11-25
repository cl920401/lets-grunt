# 按风险选验收证据 / Risk-based delivery

下面是使用示例，不是新阶段、通用验收清单或额外授权。先问：**这次承诺最可能在哪失败？什么证据能区分通过和失败？** 不因为技能看见一个例子就要求所有项目照做。

| 变更 | 最早有用证据 | 哪些发现会阻塞 |
| --- | --- | --- |
| 单机客户端 | 一条合成记录经真实持久层保存，冷启动读回，产物能独立打开核对。模拟录入界面只能证明交互。 | 数据丢失、打不开产物、验收设备不可用。没有设备是未验证，不是产品已失败。 |
| 高并发服务 | 在已约定的负载与数据集下证明并发不破坏业务不变量；故障注入覆盖关键提交窗口，观测恢复与重复副作用。可用无界面脚本。 | 超卖、重复扣款、恢复不会收敛，或测试未达到约定负载却声称通过。 |
| 数据迁移 / 契约变更 | 在隔离副本演练迁移，独立比对源目标关键指标；需要兼容时验证混合版本；演练中断、回滚或可证明的前向恢复。 | 缺数据、兼容破坏、不可逆且无准备好的恢复，不允许先迁移生产再验证。 |
| 小而可逆的界面/文案改动 | 对照准确候选的更改范围，定向检查文案或相关状态，验证应不变的行为。 | 暴露敏感信息、改变承诺或关键操作含义。可选措辞建议不阻塞。 |

Use the same distinction in reviews: a required check that did not run is not a pass and is not a failed product test. Prefer the first real result that can be checked independently, and keep later work and unchanged behavior in separate scope. A test result is not authority to deploy, access outside the project, or rewrite a pinned contract.

## 参考与取舍 / Sources and adaptations

- [GitHub Spec Kit task template](https://github.com/github/spec-kit/blob/main/templates/tasks-template.md): independently checkable increments and explicit dependencies. Adopt the evidence principle, not its task template or optional tooling.
- [OpenSpec concepts](https://github.com/Fission-AI/OpenSpec/blob/main/docs/concepts.md) and [verification](https://github.com/Fission-AI/OpenSpec/blob/main/docs/commands.md): describe deltas and check them against implementation. Preserve Let's Grunt's own pinned-version and authorization gates instead of copying archive/sync or optional verification.
- [Kubernetes KEP template](https://github.com/kubernetes/enhancements/blob/master/keps/NNNN-kep-template/README.md): deeper test, observability, compatibility and recovery questions for high-impact changes. Apply when warranted, not to every task.
- [Google Engineering Practices: code review standard](https://google.github.io/eng-practices/review/reviewer/standard.html): separate feedback worth acting on now from optional polish. Keep required acceptance and independent review.
