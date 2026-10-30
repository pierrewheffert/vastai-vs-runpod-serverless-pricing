#!/usr/bin/env python3
"""
Vast.ai vs RunPod Serverless & Managed Worker Cost Calculator 2026.
Analyzes idle cost vs active execution pricing for production AI workloads.
"""
import argparse

def evaluate_serverless(invocations, avg_duration_sec, runpod_sec_rate, dedicated_monthly_cost):
    active_seconds = invocations * avg_duration_sec
    serverless_monthly = active_seconds * runpod_sec_rate
    savings_vs_dedicated = dedicated_monthly_cost - serverless_monthly
    return {
        "active_seconds": active_seconds,
        "serverless_monthly": serverless_monthly,
        "savings_vs_dedicated": savings_vs_dedicated
    }

def main():
    parser = argparse.ArgumentParser(description="Serverless vs Dedicated GPU Cost Evaluator")
    parser.add_argument("--invocations", type=float, default=50000.0, help="Monthly API requests (default: 50,000)")
    parser.add_argument("--duration", type=float, default=2.5, help="Average duration per request in seconds (default: 2.5)")
    parser.add_argument("--rate", type=float, default=0.00045, help="RunPod Serverless per-second rate (default: $0.00045 for RTX 4090)")
    parser.add_argument("--dedicated", type=float, default=320.0, help="Monthly cost of 24/7 dedicated instance (default: $320.00)")
    args = parser.parse_args()

    res = evaluate_serverless(args.invocations, args.duration, args.rate, args.dedicated)
    print(f"Total Compute Time:      {res['active_seconds']:.1f} seconds")
    print(f"Serverless Monthly Cost: ${res['serverless_monthly']:.2f}")
    print(f"24/7 Dedicated Cost:     ${args.dedicated:.2f}")
    print(f"Net Monthly Savings:     ${res['savings_vs_dedicated']:.2f}")

if __name__ == "__main__":
    main()
