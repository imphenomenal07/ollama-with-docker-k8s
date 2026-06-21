ollama-k8s/
│
├── README.md
├── .gitignore
│
├── kubernetes/
│   ├── namespace.yaml
│   ├── pv.yaml
│   ├── pvc.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── helm/
│   └── ollama/
│       ├── Chart.yaml
│       ├── values.yaml
│       └── templates/
│           ├── deployment.yaml
│           ├── service.yaml
│           ├── pvc.yaml
│           └── ingress.yaml
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── outputs.tf
│   └── ec2.tf
│
├── scripts/
│   ├── install-models.sh
│   ├── healthcheck.sh
│   └── deploy.sh
│
├── monitoring/
│   ├── prometheus-servicemonitor.yaml
│   └── grafana-dashboard.json
│
└── docs/
    ├── architecture.md
    ├── deployment-guide.md
    └── troubleshooting.md
